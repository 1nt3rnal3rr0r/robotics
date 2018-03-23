import React, { Component } from 'react';
import Button from 'material-ui/Button';
import TextField from 'material-ui/TextField';
import { withStyles } from 'material-ui/styles';
import PropTypes from 'prop-types';

import LanguageSelector from './LanguageSelector';
import { BULGARIAN_SYMBOLS, ENGLISH_SYMBOLS, BG_LANG, EN_LANG } from './constants';
import styles from './content.styles';

class ManualInput extends Component {
  constructor(props) {
    super(props);

    this.handleLanguageChange = this.handleLanguageChange.bind(this);

    this.state = {
      manualMessage: '',
      language: EN_LANG,
    };
  }

  handleTextFieldChange(newText) {
    this.setState({ manualMessage: newText });
  }

  handleLanguageChange(language) {
    this.setState({ language });
  }

  isMessageValid() {
    if (this.state.manualMessage.length === 0) {
      return false;
    }

    for (let index = 0; index < this.state.manualMessage.length; index += 1) {
      const letter = this.state.manualMessage[index].toLowerCase();
      if (this.state.language === EN_LANG && ENGLISH_SYMBOLS.includes(letter) === false) {
        return false;
      }

      if (this.state.language === BG_LANG && BULGARIAN_SYMBOLS.includes(letter) === false) {
        return false;
      }
    }

    return true;
  }

  render() {
    const { classes } = this.props;
    const isValid = this.isMessageValid();
    return (
      <div className={classes.root}>
        <TextField
          error={!isValid}
          label={isValid ? 'Текст' : 'Невалиден текст!'}
          placeholder="някакъв текст"
          multiline
          rows="4"
          margin="normal"
          onChange={e => this.handleTextFieldChange(e.target.value)}
        />
        <LanguageSelector
          language={this.state.language}
          handleLanguageChange={this.handleLanguageChange}
        />
        <Button
          disabled={!isValid}
          variant="raised"
          size="large"
          color="primary"
          className={classes.button}
          onClick={() => this.props.sendMessage(this.state.manualMessage, this.state.language)}
        >
          Изпрати ръчно въведения текст
        </Button>
      </div>
    );
  }
}

ManualInput.propTypes = {
  classes: PropTypes.object.isRequired,
  sendMessage: PropTypes.func.isRequired,
};

export default withStyles(styles)(ManualInput);
