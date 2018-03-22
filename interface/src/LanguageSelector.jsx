import React from 'react';
import TextField from 'material-ui/TextField';
import MenuItem from 'material-ui/Menu/MenuItem';
import PropTypes from 'prop-types';

import { BG_LANG, EN_LANG } from './constants';

const LanguageSelector = ({ language, handleLanguageChange }) => (
  <TextField
    select
    label="Език"
    value={language}
    onChange={e => handleLanguageChange(e.target.value)}
    margin="normal"
  >
    <MenuItem value={BG_LANG}>Български</MenuItem>
    <MenuItem value={EN_LANG}>Английски</MenuItem>
  </TextField>
);

LanguageSelector.propTypes = {
  language: PropTypes.string.isRequired,
  handleLanguageChange: PropTypes.func.isRequired,
};

export default LanguageSelector;
