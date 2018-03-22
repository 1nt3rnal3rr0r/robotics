import React, { Component } from 'react';
import { MuiThemeProvider, createMuiTheme, withStyles } from 'material-ui/styles';
import purple from 'material-ui/colors/purple';
import green from 'material-ui/colors/green';
import CssBaseline from 'material-ui/CssBaseline';
import Paper from 'material-ui/Paper';
import PropTypes from 'prop-types';
import axios from 'axios';
import Tabs, { Tab } from 'material-ui/Tabs';
import AppBar from 'material-ui/AppBar';

import AutomaticInput from './AutomaticInput';
import ManualInput from './ManualInput';

const styles = {
  root: {
    width: '100%',
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
    alignContent: 'center',
    textAlign: 'center',
    overflow: 'auto',
    flexShrink: 0,
  },
  button: {
    marginTop: '1em',
  },
};

class App extends Component {
  static getTheme() {
    return createMuiTheme({
      palette: {
        primary: purple,
        secondary: green,
        type: 'dark',
      },
    });
  }

  static sendMessage(message, language) {
    axios
      .post(`https://${window.location.hostname}:4000/message`, {
        message,
        language,
      })
      .then(res => console.log(res.data.message))
      .catch(err => console.log(err.message));
  }

  constructor(props) {
    super(props);

    this.state = {
      tabValue: 0,
    };
  }

  handleTabChange(tabValue) {
    this.setState({ tabValue });
  }

  render() {
    const { classes } = this.props;
    const { tabValue } = this.state;

    return (
      <MuiThemeProvider theme={App.getTheme()}>
        <CssBaseline />
        <Paper className={classes.root}>
          <AppBar position="static" color="default">
            <Tabs
              value={tabValue}
              onChange={(event, value) => this.handleTabChange(value)}
              indicatorColor="primary"
              textColor="primary"
              centered
            >
              <Tab label="Автоматично диктуване" />
              <Tab label="Ръчно диктуване" />
            </Tabs>
          </AppBar>
          {tabValue === 0 && <AutomaticInput sendMessage={App.sendMessage} />}
          {tabValue === 1 && <ManualInput sendMessage={App.sendMessage} />}
        </Paper>
      </MuiThemeProvider>
    );
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(App);
