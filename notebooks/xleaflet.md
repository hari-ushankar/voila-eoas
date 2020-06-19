---
jupytext:
  formats: ipynb,py:percent
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: C++14
  language: C++14
  name: xcpp14
---

## Using voila with the C++ kernel and interactive widgets

```{code-cell}
#include <iostream>
#include <string>

#include "xwidgets/xoutput.hpp"

#include "xleaflet/xmap.hpp"
#include "xleaflet/xdraw_control.hpp"
#include "xleaflet/xbasemaps.hpp"

namespace nl = nlohmann;
```

```{code-cell}
// Create map widget
auto water_color = xlf::basemap({"OpenStreetMap", "France"});

auto map = xlf::map::initialize()
    .layers({water_color})
    .center({47, 363})
    .zoom(5)
    .finalize();

map
```

```{code-cell}
// Create output widget to log draw events
xw::output out;
out
```

```{code-cell}
// Options for the draw control
nl::json polyline_options = {
    {"shapeOptions", {
        {"color", "#6bc2e5"},
        {"weight", 8},
        {"opacity", 1.0}
    }}
};

nl::json polygon_options = {
    {"shapeOptions", {
        {"fillColor", "#6be5c3"},
        {"color", "#6be5c3"},
        {"fillOpacity", 1.0}
    }},
    {"drawError", {
        {"color", "#dd253b"},
        {"message", "Oups!"}
    }},
    {"allowIntersection", false}
};

nl::json circle_options = {
    {"shapeOptions", {
        {"fillColor", "#efed69"},
        {"fillOpacity", 1.0},
        {"color", "#efed69"}
    }}
};

nl::json rectangle_options = {
    {"shapeOptions", {
        {"fillColor", "#fca45d"},
        {"fillOpacity", 1.0},
        {"color", "#fca45d"}
    }}
};
```

```{code-cell}
// Log last action
void print_draw_event(std::string action, nl::json geo_json)
{
    // Capturing the stdout with the output widget 
    auto guard = out.guard();
    std::cout << action << " a " 
        << geo_json["geometry"]["type"]
        << std::endl;
}
```

```{code-cell}
// Add the draw control and event logger
auto draw_control = xlf::draw_control::initialize()
    .polyline(polyline_options)
    .polygon(polygon_options)
    .circle(circle_options)
    .rectangle(rectangle_options)
    .finalize();

draw_control.on_draw(print_draw_event);
map.add_control(draw_control);
```

```{code-cell}

```
