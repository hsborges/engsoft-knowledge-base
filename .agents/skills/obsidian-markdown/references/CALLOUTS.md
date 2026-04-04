# Callouts Reference

## Basic Callout

```markdown
> [!note]
> This is a note callout.

> [!info] Custom Title
> This callout has a custom title.

> [!tip] Title Only
```

## Foldable Callouts

```markdown
> [!faq]- Collapsed by default
> This content is hidden until expanded.

> [!faq]+ Expanded by default
> This content is visible but can be collapsed.
```

## Nested Callouts

```markdown
> [!question] Outer callout
> > [!note] Inner callout
> > Nested content
```

## Supported Callout Types

- `note`: aliases `-`; color/icon Blue, pencil
- `abstract`: aliases `summary`, `tldr`; color/icon Teal, clipboard
- `info`: aliases `-`; color/icon Blue, info
- `todo`: aliases `-`; color/icon Blue, checkbox
- `tip`: aliases `hint`, `important`; color/icon Cyan, flame
- `success`: aliases `check`, `done`; color/icon Green, checkmark
- `question`: aliases `help`, `faq`; color/icon Yellow, question mark
- `warning`: aliases `caution`, `attention`; color/icon Orange, warning
- `failure`: aliases `fail`, `missing`; color/icon Red, X
- `danger`: aliases `error`; color/icon Red, zap
- `bug`: aliases `-`; color/icon Red, bug
- `example`: aliases `-`; color/icon Purple, list
- `quote`: aliases `cite`; color/icon Gray, quote

## Custom Callouts (CSS)

```css
.callout[data-callout="custom-type"] {
  --callout-color: 255, 0, 0;
  --callout-icon: lucide-alert-circle;
}
```
