#import "@preview/suiji:0.4.0": *

#let cyberdream = (
  "bg": rgb("#16181a"),
  "bg_alt": rgb("#1e2124"),
  "bg_highlight": rgb("#3c4048"),
  "fg": rgb("#ffffff"),
  "grey": rgb("#7b8496"),
  "blue": rgb("#5ea1ff"),
  "green": rgb("#5eff6c"),
  "cyan": rgb("#5ef1ff"),
  "red": rgb("#ff6e5e"),
  "yellow": rgb("#f1ff5e"),
  "magenta": rgb("#ff5ef1"),
  "pink": rgb("#ff5ea0"),
  "orange": rgb("#ffbd5e"),
  "purple": rgb("#bd5eff"),
)

#let num_colors = (
  "blue",
  "green",
  "cyan",
  "red",
  "yellow",
  "magenta",
  "pink",
  "orange",
  "purple",
).map(c => cyberdream.at(c))

#let dims = (width: 2256pt, height: 1504pt)
#set page(..dims, fill: cyberdream.bg, margin: 0pt)
#set text(font: "Bauhaus 93", size: 60pt, fill: cyberdream.cyan)

#let rng = gen-rng-f(42)

#let all_cont = {
  for _ in range(54) {
    let num = 0
    let decider
    (rng, decider) = random-f(rng)
    if decider < 0.3 {
      (rng, num) = integers-f(rng, low: 0, high: 10)
    } else if decider < 0.5 {
      (rng, num) = integers-f(rng, low: 0, high: 100)
    } else if decider < 0.75 {
      (rng, num) = integers-f(rng, low: 0, high: 1000)
    } else {
      (rng, num) = integers-f(rng, low: 0, high: 10000)
      num /= 100
    }
    (rng, decider) = random-f(rng)
    if decider < 0.1 {
      num *= -1
    }
    let num_scale
    (rng, num_scale) = normal-f(rng, loc: 1, scale: 0.4)
    num_scale = calc.max(num_scale, 0.5)
    let num_rotation
    (rng, num_rotation) = uniform-f(rng, low: -30, high: 30)
    let num_color
    (rng, num_color) = choice-f(rng, num_colors)
    let cont = rotate(num_rotation * 1deg, scale(num_scale * 100%, text(
      fill: num_color,
      repr(num),
    )))
    // let dx
    // (rng, dx) = integers-f(
    //   rng,
    //   low: -calc.floor(dims.width.pt() / 2 * 0.9),
    //   high: calc.floor(dims.width.pt() / 2 * 0.9),
    // )
    // let dy
    // (rng, dy) = integers-f(
    //   rng,
    //   low: -calc.floor(dims.height.pt() / 2 * 0.9),
    //   high: calc.floor(dims.height.pt() / 2 * 0.9),
    // )
    // place(center + horizon, cont, dx: dx * 1pt, dy: dy * 1pt)
    let dx
    (rng, dx) = integers-f(
      rng,
      low: 50,
      high: 75,
    )
    h(dx * 1pt)
    box(cont, inset: 50pt)
    h(dx * 1pt)
  }
}

#place(center + horizon, scale(100%, all_cont))
