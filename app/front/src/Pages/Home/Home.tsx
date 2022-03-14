import React from "react";
import "./Home.scss";
import { Button } from "@material-ui/core";
import { useHistory } from "react-router-dom";

function Home() {
  let history = useHistory();

  return (
    <div id="buttons-screen">
      <img height={"300px"} alt="a" src="/logo.svg" />
      <div id="buttons">
        <Button
          variant="contained"
          color="primary"
          onClick={() => history.push("/data")}
        >
          CALCULATE YOUR PRICE
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => history.push("/list")}
        >
          SHOW YOUR HOUSES
        </Button>
      </div>
    </div>
  );
}

export default Home;
