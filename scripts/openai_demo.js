// AI API 配置
const config = {
  openaiApiKey: "sk-proj-2mIgLMuGyNK29jc27HfbiIYfp7nMnTdIaOwJdLcnSe",
  mistralApiKey: "ms-mpzE0KtyCZX22BJKvjgO5N1WknMGLvNv",
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
