# GitHub Release Flow

## GitHub role

GitHub is the stable public-facing release layer.

It is not:

- the raw archive
- the internal review workspace
- the client-delivery workspace

## Required flow

Every public page should pass this sequence:

1. **Raw source**
   Original PDFs, screenshot captures, exports, and experiment materials
2. **Reviewed Notion page**
   Readable internal page with filtered wording
3. **Client-safe or public-safe rewrite**
   Stable external wording with sensitive details removed
4. **GitHub public layer**
   Public-safe summary, findings page, report snapshot, or research-facing note

## Forbidden shortcuts

Do not:

- publish raw files directly to GitHub
- copy internal analysis directly into GitHub
- expose complete method detail just because it reads well
- use GitHub as the first place where a draft becomes public

## Public-safe file types

Recommended GitHub file types:

- README
- findings summaries
- report snapshots
- evidence-chain notes
- known-limits pages
- scope-and-disclosure pages
- concept notes
- citation metadata

## Release decision test

Before writing to GitHub, ask:

1. Is this already safe outside Notion?
2. Does this page describe observation rather than internal detail?
3. Would this wording reveal too much about the private side of the workflow?
4. Is this page better as a public summary than as a raw artifact?

If any answer is unsafe, keep the material upstream.
