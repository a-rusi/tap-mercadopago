# tap-mercadopago

`tap-mercadopago` is a Singer tap for MercadoPago.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
pipx install git+https://github.com/a-rusi/tap-mercadopago.git
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-mercadopago --about
```

### Source Authentication and Authorization

The only config that's a strict requirement for this app is your Mercado Pago's `auth_token`.
You can find more info about creating an application and getting your `auth_token` [here](https://www.mercadopago.com.ar/developers/es/guides/overview)

## Usage

You can easily run `tap-mercadopago` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-mercadopago --version
tap-mercadopago --help
tap-mercadopago --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-mercadopago
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-mercadopago --version
# OR run a test `elt` pipeline:
meltano elt tap-mercadopago target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
