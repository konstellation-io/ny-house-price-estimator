import React, { useEffect } from "react";
import "./DataForm.scss";

import { useForm } from "react-hook-form";

import {
  Button,
  TextField,
  InputAdornment,
  FormControl,
  FormControlLabel,
  Checkbox,
  Select,
  InputLabel,
  MenuItem,
} from "@material-ui/core";
import {
  AccountCircle,
  MeetingRoom,
  Hotel,
  Bathtub,
  List,
  Home,
} from "@material-ui/icons";
import MapWrapper from "../../Components/MapWrapper/MapWrapper";
import useLocalStorage from "../../Hooks/useLocalStorage";
import { useHistory } from "react-router";
import { API_BASE_URL } from "../../index";
import { ErrorModal } from "../../Components/Modal/Error/ErrorModal";
import useAxios from "axios-hooks";

// Constants
import { API_MAKE_PREDICTION } from "../../Constants/api";
import { CALL_LIST } from "../../Constants/localStorage";
import { ROUTE_DETAIL, ROUTE_HOME, ROUTE_LIST } from "../../Constants/routes";

function DataForm() {
  const history = useHistory();
  const [callList, setCallList] = useLocalStorage(CALL_LIST, []);
  const [openErrorModal, setOpenErrorModal] = React.useState(false);
  const [{ error }, makeRequest] = useAxios(
    {
      url: `${API_BASE_URL}${API_MAKE_PREDICTION}`,
      method: "post",
    },
    { manual: true }
  );

  const room_types = [
    "Shared room",
    "Private room",
    "Entire home/apt",
    "Hotel room",
  ];

  const neighbourhoods = [
    "Bronx",
    "Queens",
    "Staten Island",
    "Brooklyn",
    "Manhattan",
  ];

  const { register, handleSubmit, watch, setValue, errors } = useForm({
    defaultValues: {
      bedrooms: 1,
      beds: 1,
      accommodates: 1,
      bathrooms: 1,
      room_type: room_types[0],
      neighbourhood: neighbourhoods[0],
      tv: 0,
      elevator: 0,
      internet: 0,
      latitude: 40.791269430732555,
      longitude: -73.96330053394196,
    },
  });

  useEffect(() => {
    register("room_type");
    register("neighbourhood");
    register("latitude");
    register("longitude");
    register("tv");
    register("elevator");
    register("internet");
  }, [register]);

  const setCoords = (coords: { latitude: number; longitude: number }) => {
    setValue("latitude", coords.latitude);
    setValue("longitude", coords.longitude);
  };

  const onSubmit = async (submitData: any) => {
    try {
      // Property name must be deleted
      const dataToSend = { ...submitData };
      delete dataToSend["name"];

      const { data } = await makeRequest({
        data: {
          ...dataToSend,
        },
      });

      const { category, market_price } = data;
      submitData["predicted_category"] = category;
      submitData["market_price"] = market_price;
      submitData["date"] = Date.now();

      const newCallList = [...callList, submitData];
      setCallList(newCallList);
      history.push(
        ROUTE_DETAIL.replace(":position", (newCallList.length - 1).toString())
      );
    } catch (e) {
      setOpenErrorModal(true);
      console.log(e);
    }
  };

  return (
    <div className="data-form">
      <ErrorModal
        open={openErrorModal}
        close={() => setOpenErrorModal(false)}
        error={error}
      />
      <div id="logo-group">
        <img src="/logo.svg" alt={"Logo"} />
        <h1>Describe your house</h1>
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
            id="houses-list-btn"
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
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="input-fields">
          <TextField
            className="name-input"
            name="name"
            label="Name"
            required
            variant="filled"
            color="secondary"
            type="text"
            inputRef={register}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <MeetingRoom />
                </InputAdornment>
              ),
            }}
          />
          <FormControl variant="filled" className="type-select">
            <InputLabel shrink id="room-type-label">
              Room Type
            </InputLabel>
            <Select
              name="room_type"
              value={watch("room_type")}
              onChange={(event: any) =>
                setValue("room_type", event.target.value)
              }
            >
              {room_types.map((value) => {
                return (
                  <MenuItem value={value} key={value}>
                    {value}
                  </MenuItem>
                );
              })}
            </Select>
          </FormControl>
          <FormControl variant="filled" className="type-select">
            <InputLabel shrink id="neighbourhood-label">
              Neighbourhood
            </InputLabel>
            <Select
              name="neighbourhood"
              value={watch("neighbourhood")}
              onChange={(event: any) =>
                setValue("neighbourhood", event.target.value)
              }
            >
              {neighbourhoods.map((value) => {
                return (
                  <MenuItem value={value} key={value}>
                    {value}
                  </MenuItem>
                );
              })}
            </Select>
          </FormControl>
          <TextField
            id="bedrooms-input"
            name="bedrooms"
            label="Bedrooms"
            required
            variant="filled"
            color="secondary"
            type="number"
            inputRef={(e) => register(e, { min: 0 })}
            error={errors.bedrooms ? true : false}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <MeetingRoom />
                </InputAdornment>
              ),
            }}
          />
          <TextField
            id="beds-input"
            name="beds"
            label="Beds"
            required
            variant="filled"
            color="secondary"
            type="number"
            inputRef={(e) => register(e, { min: 0 })}
            error={errors.beds ? true : false}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <Hotel />
                </InputAdornment>
              ),
            }}
          />
          <TextField
            id="accommodates-input"
            name="accommodates"
            label="Accommodates"
            required
            variant="filled"
            color="secondary"
            type="number"
            inputRef={(e) => register(e, { min: 0 })}
            error={errors.accommodates ? true : false}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <AccountCircle />
                </InputAdornment>
              ),
            }}
          />
          <TextField
            id="bathrooms-input"
            name="bathrooms"
            label="Bathrooms"
            required
            variant="filled"
            color="secondary"
            type="number"
            inputRef={(e) => register(e, { min: 0 })}
            error={errors.bathrooms ? true : false}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <Bathtub />
                </InputAdornment>
              ),
            }}
          />
        </div>

        <div>
          <FormControlLabel
            label="TV"
            name="tv"
            value={watch("tv")}
            onChange={(event: any) =>
              setValue("tv", Number(event.target.checked))
            }
            control={<Checkbox name="tv" color="secondary" />}
          />

          <FormControlLabel
            label="Elevator"
            name="elevator"
            value={watch("elevator")}
            onChange={(event: any) =>
              setValue("elevator", Number(event.target.checked))
            }
            control={<Checkbox name="elevator" color="secondary" />}
          />
          <FormControlLabel
            label="Internet"
            name="internet"
            value={watch("internet")}
            onChange={(event: any) =>
              setValue("internet", Number(event.target.checked))
            }
            control={<Checkbox name="internet" color="secondary" />}
          />
        </div>
        <MapWrapper
          className="map-wrapper"
          latitude={watch("latitude")}
          longitude={watch("longitude")}
          draggable={true}
          setMarkerPosition={(coords: any) => setCoords(coords)}
        />
        <Button variant="contained" color="secondary" type="submit">
          ESTIMATE
        </Button>
      </form>
    </div>
  );
}

export default DataForm;
