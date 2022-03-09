---
title: REST API
---
# 

<div id="swagger-ui" style="background-color:white;"></div>

<script>
window.onload = function() {
  const ui = SwaggerUIBundle({
    url: "https://app.qfield.cloud/swagger.yaml",
    dom_id: '#swagger-ui',
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ]
  })

  window.ui = ui
}
</script>
