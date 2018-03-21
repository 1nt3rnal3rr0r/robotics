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
import TextField from 'material-ui/TextField';
import MenuItem from 'material-ui/Menu/MenuItem';

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
  form: {
    margin: 'auto',
    flexShrink: 0,
    display: 'flex',
    alignItems: 'center',
    flexDirection: 'column',
    overflow: 'auto',
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

    /* eslint no-use-before-define: 0, no-undef: 0 */
    const SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    this.recognition = new SpeechRecognition();
    this.recognition.continuous = true;
    this.recognition.interimResults = true;
    this.recognition.onresult = this.recognitionResult;
    this.recognition.onend = this.stopRecording;

    this.state = {
      transcript: '',
      isRecording: false,
      endpoint: `https://${window.location.hostname}:4000`,
      lang: 'bg-BG',
      manualMessage: '',
    };
  }

  componentWillUnmount() {
    this.recognition.stop();
  }

  startRecording() {
    this.setState({ isRecording: true });
    this.recognition.lang = this.state.lang;
    this.recognition.start();
  }

  stopRecording() {
    this.setState({ isRecording: false });
    this.recognition.stop();
  }

  sendMessage(message) {
    axios
      .post(`${this.state.endpoint}/message`, { message, language: this.state.lang })
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

  handleLanguageChange(newLang) {
    this.recognition.stop();
    this.setState({ lang: newLang });
  }

  handleTextFieldChange(newText) {
    this.setState({ manualMessage: newText });
  }

  render() {
    const { classes } = this.props;
    return (
      <MuiThemeProvider theme={App.getTheme()}>
        <CssBaseline />
        <Paper className={classes.root}>
          <div className={this.props.classes.form}>
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
              onClick={() =>
                (this.state.isRecording ? this.stopRecording() : this.startRecording())
              }
            >
              {this.state.isRecording ? 'Спри запис' : 'Започни запис'}
            </Button>
            <TextField
              select
              label="Език"
              value={this.state.lang}
              onChange={e => this.handleLanguageChange(e.target.value)}
              margin="normal"
            >
              <MenuItem value="bg-BG">Български</MenuItem>
              <MenuItem value="en-US">Английски</MenuItem>
            </TextField>
            <TextField
              label="Ръчен текст"
              placeholder="някакъв текст"
              multiline
              rows="4"
              margin="normal"
              onChange={e => this.handleTextFieldChange(e.target.value)}
            />
            <Button
              variant="raised"
              size="large"
              color="primary"
              className={classes.button}
              onClick={() => this.sendMessage(this.state.manualMessage)}
            >
              Изпрати ръчно въведения текст
            </Button>
          </div>
        </Paper>
      </MuiThemeProvider>
    );
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(App);
