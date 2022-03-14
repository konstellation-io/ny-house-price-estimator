import React from "react";
import "./HousesListItem.scss";
import moment from "moment";
import {
  AccessTime,
  AccountCircle,
  Bathtub,
  Hotel,
  MeetingRoom,
  SystemUpdateAlt,
  Tv,
  Wifi,
} from "@material-ui/icons";
import { Button, Chip } from "@material-ui/core";
import { getCategoryValues } from "../../Helpers/Categories";

export default function HousesListItem({
  handleOpen,
  value,
  index,
  onClick,
}: any) {
  const getColorFromCategory = (category: string) => {
    switch (category) {
      case "low":
        return { backgroundColor: "#fefbeb" };
      case "mid":
        return { backgroundColor: "#fef0b0" };
      case "high":
        return { backgroundColor: "#fde575" };
      case "lux":
        return { backgroundColor: "#FDDB3A" };
    }
  };

  return (
    <div id="houses-list-item" key={index} onClick={onClick}>
      <div className="name-group title-group">
        <span className="title">Name</span>
        <span>{value.name}</span>
      </div>
      <div className="date-icon-group icon-group">
        <AccessTime />
        <span>{moment(value.date).utc().from(moment(Date.now()).utc())}</span>
      </div>
      <div className="icon-group icon-group">
        <MeetingRoom />
        <span>{value.bedrooms}</span>
      </div>
      <div className="beds-icon-group icon-group">
        <Hotel />
        {value.beds}
      </div>
      <div className="accommodates-icon-group icon-group">
        <AccountCircle />
        {value.accommodates}
      </div>
      <div className="bath-icon-group icon-group">
        <Bathtub />
        {value.bathrooms}
      </div>
      <div className="tv-icon-group icon-group">
        <Tv />
        {value.tv}
      </div>
      <div className="elevator-icon-group icon-group">
        <SystemUpdateAlt />
        {value.elevator}
      </div>
      <div className="internet-icon-group icon-group">
        <Wifi />
        {value.internet}
      </div>
      <div className="predicted-category-group title-group">
        <span className="title">Predicted Value</span>
        <Chip
          style={getColorFromCategory(value.predicted_category)}
          size="small"
          label={getCategoryValues(value.predicted_category)}
          icon={<Chip label={value.predicted_category} />}
        />
      </div>
      {(() => {
        if (value.real_category)
          return (
            <div className="real-category-group title-group">
              <span className="title">Your value</span>
              <Chip
                style={getColorFromCategory(value.real_category)}
                size="small"
                label={value.real_price}
                icon={<Chip label={value.real_category} />}
              />
            </div>
          );

        return (
          <Button
            className="rented-btn"
            variant="contained"
            color="primary"
            disableElevation
            onClick={(event) => {
              event.preventDefault();
              event.stopPropagation();
              handleOpen(index);
            }}
          >
            Rented
          </Button>
        );
      })()}
    </div>
  );
}
