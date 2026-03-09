import { useState } from 'react'
import './App.css'

function App() {
  const [paragraph, setParagraph] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('http://localhost:8000/extract', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ paragraph }),
      })

      if (!response.ok) {
        throw new Error('Failed to fetch data')
      }

      const data = await response.json()
      
      // The backend returns a stringified JSON (often) inside the "result" field.
      // We attempt to parse it if it's a string, or use it directly if it's an object.
      let parsedResult = data.result;
      
      if (typeof data.result === 'string') {
        try {
           // Remove potential markdown code blocks
           const cleaned = data.result.replace(/```json\n?|```/g, '');
           parsedResult = JSON.parse(cleaned);
        } catch (e) {
           console.log("Could not parse result as JSON, displaying raw", e);
           // Keep as string if parsing fails
        }
      }

      setResult(parsedResult)

    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Movie Info Extractor</h1>
      
      <div className="card">
        <form onSubmit={handleSubmit} className="extraction-form">
          <textarea
            value={paragraph}
            onChange={(e) => setParagraph(e.target.value)}
            placeholder="Paste a paragraph about a movie here..."
            rows={6}
            className="input-area"
            required
          />
          <button type="submit" disabled={loading || !paragraph.trim()}>
            {loading ? 'Extracting...' : 'Extract Info'}
          </button>
        </form>
      </div>

      {error && <div className="error">{error}</div>}

      {result && (
        <div className="result-container">
          <h2>Extracted Information</h2>
          <div className="json-view">
             {typeof result === 'object' && result !== null ? (
                Object.entries(result).map(([key, value]) => (
                  <div key={key} className="info-row">
                    <span className="key">{key.replace(/_/g, ' ')}:</span>
                    <span className="value">
                      {Array.isArray(value) ? value.join(', ') : String(value)}
                    </span>
                  </div>
                ))
             ) : (
                <pre>{String(result)}</pre>
             )}
          </div>
        </div>
      )}
    </div>
  )
}

export default App
