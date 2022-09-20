---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Derivatives

## Definition of Derivative:

$$
\begin{aligned}
\boxed{\frac{d}{dx}(f(x)) = f^\prime(x) = \lim_{h \to 0}\frac{f(x + h) - f(x)}{h}}
\end{aligned}
$$

---

#### Derivative Rules:

```{admonition}Constant Rule:
:class: note

$$
\begin{aligned}
\frac{d}{dx}[c] = 0
\end{aligned}
$$
```

$$
\begin{gathered}
\frac{d}{dx}32 = 0 \qquad \frac{d}{dx}\pi = 0
\end{gathered}
$$

```{admonition}Power Rule:
:class: note

$$
\begin{aligned}
\frac{d}{dx}[x^n] = nx^{n - 1}
\end{aligned}
$$
```

$$
\begin{gathered}
\frac{d}{dx}n^2 = 2n \qquad \frac{d}{dx}\varphi^3 = 3 \varphi^2
\end{gathered}
$$

```{admonition}Product Rule:
:class: note

$$
\begin{aligned}
\frac{d}{dx}[f(x)g(x)] = f^\prime(x)g(x) + f(x)g^\prime(x)
\end{aligned}
$$
```

```{admonition}Quotient Rule:
:class: note

$$
\begin{aligned}
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x)f^\prime(x) - f(x)g^\prime(x)}{\left[g(x)^{-2}\right]}
\end{aligned}
$$
```

```{admonition}Chain Rule:
:class: note

$$
\begin{aligned}
\frac{d}{dx}\left[f(g(x))\right] = f^\prime(g(x))g^\prime(x)
\end{aligned}
$$
```
