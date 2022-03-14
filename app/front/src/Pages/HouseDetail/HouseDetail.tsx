import React from "react";
import "./HouseDetail.scss";
import HousesListItem from "../../Components/HousesListItem/HousesListItem";

import { useParams } from "react-router-dom";
import useLocalStorage from "../../Hooks/useLocalStorage";
import { CALL_LIST } from "../../Constants/localStorage";
import MapWrapper from "../../Components/MapWrapper/MapWrapper";
import { PriceModal } from "../../Components/Modal/Price/PriceModal";
import { toCategory } from "../../Helpers/Categories";
import useAxios from "axios-hooks";
import { API_BASE_URL } from "../../index";
import { API_SAVE_METRICS } from "../../Constants/api";
import { ErrorModal } from "../../Components/Modal/Error/ErrorModal";
import { Button } from "@material-ui/core";
import { Add, Home, List } from "@material-ui/icons";
import { ROUTE_DATA, ROUTE_HOME, ROUTE_LIST } from "../../Constants/routes";
import { useHistory } from "react-router";

export function HouseDetail() {
  const history = useHistory();

  const { position } = useParams();
  const [callList, setCallList] = useLocalStorage(CALL_LIST, []);
  let call = callList[position];

  const [openPriceModal, setOpenPriceModal] = React.useState(false);
  const [openErrorModal, setOpenErrorModal] = React.useState(false);
  const [price, setPrice] = React.useState(0);

  const [{ error }, makeRequest] = useAxios(
    {
      url: `${API_BASE_URL}${API_SAVE_METRICS}`,
      method: "post",
    },
    { manual: true }
  );

  const sendRealValue = async () => {
    const callItem = callList[position];
    const realCategory = toCategory(price);
    try {
      await makeRequest({
        data: [
          {
            predicted_category: callItem.predicted_category,
            real_category: realCategory,
            date: Math.floor(Date.now() / 1000),
          },
        ],
      });

      callItem["real_category"] = realCategory;
      callItem["real_price"] = price;

      callList[position] = callItem;
      setCallList(callList);
    } catch (e) {
      setOpenErrorModal(true);
      console.log(e);
    }

    setOpenPriceModal(false);
    setPrice(0);
  };

  return (
    <div id="detail">
      <ErrorModal
        open={openErrorModal}
        close={() => setOpenErrorModal(false)}
        error={error}
      />
      <PriceModal
        open={openPriceModal}
        price={price}
        setPrice={setPrice}
        close={() => setOpenPriceModal(false)}
        sendRealValue={sendRealValue}
      />
      <div id="logo-group">
        <img src="/logo.svg" alt={"Logo"} />
        <h1>Prediction</h1>
        <div id="buttons-group">
          <Button
            variant="contained"
            color="primary"
            disableElevation
            onClick={() => history.push(ROUTE_HOME)}
            startIcon={<Home />}
          >
            Home
          </Button>
          <Button
            variant="contained"
            color="primary"
            disableElevation
            onClick={() => history.push(ROUTE_DATA)}
            startIcon={<Add />}
          >
            New
          </Button>
          <Button
            variant="contained"
            color="primary"
            disableElevation
            onClick={() => history.push(ROUTE_LIST)}
            startIcon={<List />}
          >
            List
          </Button>
        </div>
      </div>
      <div id="detail-wrapper">
        <HousesListItem
          value={call}
          handleOpen={() => setOpenPriceModal(true)}
        />
        <MapWrapper
          className="map-wrapper"
          latitude={call.latitude}
          longitude={call.longitude}
          draggable={false}
        />
      </div>
    </div>
  );
}
