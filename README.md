# Repro: product context resets on shared pages

Minimal Mintlify docs that reproduce the product switcher resetting when a shared page is opened. Filed alongside a support thread about structuring docs where some sections are product-specific and some are shared across products.

## Navigation structure

The `docs.json` nests navigation as `languages` (en, zh) > `products` (Product A, Product B) > `tabs` (Doc 1, Doc 2) > `pages`.

- **Doc 1** holds three pages that are unique to each product, under `{language}/product_a/` and `{language}/product_b/`.
- **Doc 2** is shared. Both products list the exact same page paths (`{language}/shared/billing`, `/security`, `/support`). There is a single physical copy of each shared file, referenced from both products' navigation blocks.

Product A is listed before Product B in `docs.json`.

```
en/
  product_a/  a-overview, a-install, a-usage   (Doc 1, unique to A)
  product_b/  b-overview, b-install, b-usage   (Doc 1, unique to B)
  shared/     billing, security, support       (Doc 2, referenced by A and B)
zh/
  ... mirrored
```

## Steps to reproduce

1. Open the site and select **Product B** in the product switcher.
2. While in Product B, click the **Doc 2** tab.

The redirect happens as soon as the Doc 2 tab is opened. You do not need to click an individual shared page first.

## Expected

Opening Doc 2 under Product B keeps you in Product B.

## Observed

The product switcher jumps to **Product A** the moment the Doc 2 tab is opened. Doc 2's pages resolve to the first product in `docs.json` that lists them, which is Product A, so the selected Product B context is lost.

This makes shared sections feel like they belong to whichever product appears first, and the user's product selection is not preserved when navigating to shared documentation.

## Local preview

```
npm i -g mint
mint dev
```
