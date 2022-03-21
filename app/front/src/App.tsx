import React from "react";
import "./App.scss";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { ThemeProvider } from "@material-ui/core/styles";
import Theme from "./Theme";
import CssBaseline from "@material-ui/core/CssBaseline";
import {
  ROUTE_DATA,
  ROUTE_DETAIL,
  ROUTE_HOME,
  ROUTE_LIST,
} from "./Constants/routes";
import Home from "./Pages/Home/Home";
import DataForm from "./Pages/DataForm/DataForm";
import HousesList from "./Pages/HousesList/HousesList";
import { HouseDetail } from "./Pages/HouseDetail/HouseDetail";

function App() {

  return (
    <ThemeProvider theme={Theme}>
      <CssBaseline />
      <div className="App">
        <Router>
          <Switch>
            <Route exact path={ROUTE_HOME}>
              <Home />
            </Route>
            <Route exact path={ROUTE_DATA}>
              <DataForm />
            </Route>
            <Route exact path={ROUTE_DETAIL}>
              <HouseDetail />
            </Route>
            <Route exact path={ROUTE_LIST}>
              <HousesList />
            </Route>
          </Switch>
        </Router>
      </div>
    </ThemeProvider>
  );
}

export default App;
