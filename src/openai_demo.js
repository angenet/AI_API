// AI API 配置
const config = {
  anthropicApiKey: "sk-ant-api03-CC84ZDA6Kh2kf8vGQrayb08ne5Fe6PO5ymkRS",
  xiaomi_tpApiKey: "tp-W5Gkz0Pey6VoShcoEJd3ZxUWLA100vxF",
};

async function chat(prompt, provider = 'openai') {
  const apiKey = config[provider + 'ApiKey'];
  const response = await fetch(`https://api.${provider}.com/v1/chat`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ model: 'gpt-4', messages: [{ role: 'user', content: prompt }] }),
  });
  return response.json();
}

module.exports = { config, chat };
