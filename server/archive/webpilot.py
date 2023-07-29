# Import the plugin
webpilot_plugin = langchain.import_plugin('https://webreader.webpilotai.com/openapi.yaml')

# Instantiate the plugin
webpilot = webpilot_plugin()

# Call the plugin's method
response = webpilot.visitWebPage({
  "link": "https://example.com",
  "lp": true,
  "ur": "content of website example.com",
  "l": "en",
  "rt": false
})

# Process the response
print(response)