import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [mode, setMode] = useState("brief");
  const [model, setModel] = useState("tinyllama");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    setSummary("");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("mode", mode);
    formData.append("model", model);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/summarize-stream",
        {
          method: "POST",
          body: formData,
        }
      );

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        setSummary((prev) => prev + chunk);
      }

    } catch (error) {
      console.error(error);
      setSummary("Error generating summary");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-6">📄 PDF Summarizer</h1>

      <div className="bg-white p-6 rounded-xl shadow-md w-full max-w-xl">
        
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="mb-4"
        />

        <div className="mb-4">
          <label className="block mb-1 font-medium">Mode</label>
          <select
            value={mode}
            onChange={(e) => setMode(e.target.value)}
            className="w-full border p-2 rounded"
          >
            <option value="brief">Brief</option>
            <option value="detailed">Detailed</option>
            <option value="bullet">Bullet</option>
            <option value="executive">Executive</option>
          </select>
        </div>

        <div className="mb-4">
          <label className="block mb-1 font-medium">Model</label>
          <select
            value={model}
            onChange={(e) => setModel(e.target.value)}
            className="w-full border p-2 rounded"
          >
            <option value="tinyllama">TinyLlama</option>
            <option value="mistral">Mistral</option>
          </select>
        </div>

        <button
          onClick={handleUpload}
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          {loading ? "Processing..." : "Summarize"}
        </button>

        <div className="mt-6 whitespace-pre-wrap">
          {summary}
        </div>
      </div>
    </div>
  );
}

export default App;