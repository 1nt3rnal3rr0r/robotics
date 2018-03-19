import React, { Component } from 'react';
import { MuiThemeProvider, createMuiTheme, withStyles } from 'material-ui/styles';
import purple from 'material-ui/colors/purple';
import green from 'material-ui/colors/green';
import CssBaseline from 'material-ui/CssBaseline';
import Paper from 'material-ui/Paper';
import Typography from 'material-ui/Typography';
import PropTypes from 'prop-types';
import Button from 'material-ui/Button';
import axios from 'axios';

const styles = {
  root: {
    width: '100%',
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    alignContent: 'center',
    textAlign: 'center',
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

  constructor(props) {
    super(props);

    this.recognitionResult = this.recognitionResult.bind(this);
    this.stopRecording = this.stopRecording.bind(this);
    this.sendMessage = this.sendMessage.bind(this);

    /* eslint no-use-before-define: 0, no-undef: 0 */
    const SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.lang = 'bg-BG';
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onresult = this.recognitionResult;
    recognition.onend = this.stopRecording;

    this.state = {
      recognition,
      transcript: '',
      isRecording: false,
      endpoint: `http://${window.location.hostname}:4000`,
    };
  }

  componentWillUnmount() {
    this.state.recognition.stop();
  }

  startRecording() {
    this.setState({ isRecording: true });
    this.state.recognition.start();
  }

  stopRecording() {
    this.setState({ isRecording: false });
    this.state.recognition.stop();
  }

  sendMessage(message) {
    axios
      .post(`${this.state.endpoint}/message`, { message })
      .then(res => console.log(res.data.message))
      .catch(err => console.log(err.message));
  }

  recognitionResult(event) {
    let finalTranscript = '';
    let interimTranscript = '';
    for (let i = event.resultIndex; i < event.results.length; i += 1) {
      if (event.results[i].isFinal) {
        finalTranscript += event.results[i][0].transcript;
      } else {
        interimTranscript += event.results[i][0].transcript;
      }
    }

    if (finalTranscript !== '') {
      this.setState({ transcript: finalTranscript });
      this.sendMessage(finalTranscript);
    } else {
      this.setState({ transcript: interimTranscript });
    }
  }

  render() {
    const { classes } = this.props;
    return (
      <MuiThemeProvider theme={App.getTheme()}>
        <CssBaseline />
        <Paper className={classes.root}>
          {this.state.transcript !== '' && (
            <Typography variant="headline" component="h3">
              {this.state.transcript}
            </Typography>
          )}
          <Button
            variant="raised"
            size="large"
            color="primary"
            className={classes.button}
            onClick={() => (this.state.isRecording ? this.stopRecording() : this.startRecording())}
          >
            {this.state.isRecording ? 'Спри запис' : 'Започни запис'}
          </Button>
        </Paper>
      </MuiThemeProvider>
    );
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(App);
