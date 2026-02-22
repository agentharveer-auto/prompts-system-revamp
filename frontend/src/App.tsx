import React, { useEffect, useState } from 'react'

type Prompt = { id: string; title: string; content: string; owner: string; created_at: string; updated_at: string; tags: string[] };

function App() {
  const [prompts, setPrompts] = useState<Prompt[]>([])

  useEffect(() => {
    fetch('/prompts')
      .then(res => res.json())
      .then((data) => setPrompts(data))
      .catch(() => {})
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>Prompts Catalog (V2 MVP)</h1>
      <ul>
        {prompts.map(p => (
          <li key={p.id}>
            <strong>{p.title}</strong> by {p.owner}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
