import React from "react";
import "./HousesList.scss";

import useLocalStorage from "../../Hooks/useLocalStorage";
import useAxios from "axios-hooks";
import HousesListItem from "../../Components/HousesListItem/HousesListItem";
import { API_BASE_URL } from "../../index";
import { ErrorModal } from "../../Components/Modal/Error/ErrorModal";
import { toCategory } from "../../Helpers/Categories";

// Constants
import { CALL_LIST } from "../../Constants/localStorage";
import { API_SAVE_METRICS } from "../../Constants/api";
import { PriceModal } from "../../Components/Modal/Price/PriceModal";
import { useHistory } from "react-router";
import { ROUTE_DATA, ROUTE_DETAIL, ROUTE_HOME } from "../../Constants/routes";
import { Button } from "@material-ui/core";
import { Add, Home } from "@material-ui/icons";

function HousesList() {
  const history = useHistory();
  const [callList, setCallList] = useLocalStorage(CALL_LIST, []);
  const [{ error }, makeRequest] = useAxios(
    {
      url: `${API_BASE_URL}${API_SAVE_METRICS}`,
      method: "post",
    },
    { manual: true }
  );
  const [openPriceModal, setOpenPriceModal] = React.useState(false);
  const [openErrorModal, setOpenErrorModal] = React.useState(false);
  const [price, setPrice] = React.useState(0);
  const [position, setPosition] = React.useState(-1);

  const handleOpenPriceModal = (index: number) => {
    setOpenPriceModal(true);
    setPosition(index);
  };

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

  const goToDetail = (position: string) => {
    history.push(ROUTE_DETAIL.replace(":position", position));
  };

  return (
    <div>
      <ErrorModal
        open={openErrorModal}
        close={() => setOpenErrorModal(false)}
        error={error}
      />
      <PriceModal
        open={openPriceModal}
        close={() => setOpenPriceModal(false)}
        setPrice={setPrice}
        price={price}
        sendRealValue={sendRealValue}
      />
      <div id="houses-list-screen">
        <div id="logo-group">
          <img alt="a" src="/logo.svg" />
          <h1>Houses List</h1>
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
          </div>
        </div>

        <div id="houses-list">
          {[...callList].reverse().map((value: any, index: number) => {
            const position = callList.length - (index + 1);
            return (
              <HousesListItem
                onClick={() => goToDetail(position.toString())}
                key={position}
                handleOpen={handleOpenPriceModal}
                value={value}
                index={position}
              />
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default HousesList;
