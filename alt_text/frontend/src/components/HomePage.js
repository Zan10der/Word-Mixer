import React, { Component } from "react";

import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,
} from "react-router-dom";


export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    renderHomePage() {
        return (
            <Typography variant="h3">
            brsk - Alt Text
        </Typography>
        );
    }

    render() {
        return (
            this.renderHomePage()
        )
    }
}