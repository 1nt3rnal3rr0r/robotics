import React, { Component } from 'react';
import Typography from 'material-ui/Typography';
import Button from 'material-ui/Button';
import { withStyles } from 'material-ui/styles';
import PropTypes from 'prop-types';

import LanguageSelector from './LanguageSelector';
import { EN_LANG } from '../constants';
import styles from './content.styles';

class AutomaticInput extends Component {
  constructor(props) {
    super(props);

    this.handleLanguageChange = this.handleLanguageChange.bind(this);
    this.stopRecording = this.stopRecording.bind(this);
    this.recognitionResult = this.recognitionResult.bind(this);

    /* eslint no-use-before-define: 0, no-undef: 0 */
    const SpeechRecognition = webkitSpeechRecognition;
    this.recognition = new SpeechRecognition();
    this.recognition.continuous = true;
    this.recognition.interimResults = true;
    this.recognition.onresult = this.recognitionResult;
    this.recognition.onend = this.stopRecording;

    this.state = {
      transcript: '',
      isRecording: false,
      language: EN_LANG,
    };
  }

  componentWillUnmount() {
    this.recognition.stop();
  }

  handleLanguageChange(language) {
    this.recognition.stop();
    this.setState({ language });
  }

  startRecording() {
    this.setState({ isRecording: true });
    this.recognition.lang = this.state.language;
    this.recognition.start();
  }

  stopRecording() {
    this.setState({ isRecording: false });
    this.recognition.stop();
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
      this.props.sendMessage(finalTranscript, this.state.language);
    } else {
      this.setState({ transcript: interimTranscript });
    }
  }

  render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        {this.state.transcript !== '' && (
          <Typography variant="headline" component="h3">
            {this.state.transcript}
          </Typography>
        )}
        <LanguageSelector
          language={this.state.language}
          handleLanguageChange={this.handleLanguageChange}
        />
        <Button
          variant="raised"
          size="large"
          color="primary"
          className={classes.button}
          onClick={() => (this.state.isRecording ? this.stopRecording() : this.startRecording())}
        >
          {this.state.isRecording ? 'Спри запис' : 'Започни запис'}
        </Button>
      </div>
    );
  }
}

AutomaticInput.propTypes = {
  classes: PropTypes.object.isRequired,
  sendMessage: PropTypes.func.isRequired,
};

export default withStyles(styles)(AutomaticInput);
