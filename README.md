# Payment UI

## Quick start

### Docker

This app supports the HM Land Registry [common dev-env](https://github.com/LandRegistry/common-dev-env) so adding the following to your dev-env config file is enough:

```YAML
  payment-ui:
    repo: git@github.com:LandRegistry/digital-street-payment-ui.git
    branch: master
```

The Docker image it creates (and runs) will install all necessary requirements and set all environment variables for you.
