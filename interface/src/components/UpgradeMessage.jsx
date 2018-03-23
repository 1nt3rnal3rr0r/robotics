import React from 'react';
import Typography from 'material-ui/Typography';
import { withStyles } from 'material-ui/styles';
import PropTypes from 'prop-types';

import styles from './content.styles';

const UpgradeMessage = ({ classes }) => (
  <Typography variant="display3" className={classes.root}>
    {' '}
    Трябва ви Google Chrome 25+, за да ползвате тази функционалност.
  </Typography>
);

UpgradeMessage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(UpgradeMessage);
