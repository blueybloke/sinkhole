# Sinkhole (WIP)

Sinkhole is a WIP CLI tool for creating and managing **event sinks** and **webhooks** for **Nomad > v1.0**

## Why?
If you are running a Nomad cluster it can be helpful to have a generic way to do things when an event occurs.
For example, if one of your jobs fails you might want it to trigger a message in Slack, run CI on the commit, ~~or fire the developer responsible.~~

## How it works
Sinkhole uses the [Nomad event API](https://www.nomadproject.io/api-docs/events) that will be released in version 1.0.0. Because of this, it is not yet available, and if you want to use it you will need to download the 1.0.0 beta of Nomad. At the moment it just uses Click and Requests to access the API, and register event sinks on the Nomad agent, and then link those sinks to webhook URL(s). Nomad will then handle forwarding any requests to the relevant URLs, which can be for [Slack](https://api.slack.com/messaging/webhooks), something you made yourself or any other piece of software that supports this.

## Installation (Not ready)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sinkhole.

```bash
pip install sinkhole
```

## Usage

*Coming soon...*


## License
[MIT](https://choosealicense.com/licenses/mit/)
