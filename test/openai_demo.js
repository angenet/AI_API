// AI API 配置
const config = {
  openaiApiKey: "sk-proj-i9Z3lh98DTWTSiMdvvytHIWN0I8pEAjSY9izZegkLJ",
  xiaomi_tpApiKey: "tp-eZIrjr8rQDjix9B4z9HNynizeMY6QsdK",
  volcanoApiKey: "c1365eec-fd56-4232-8d72-71a6cf7786a4",
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
