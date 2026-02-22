export function formatPromptTitle(title: string): string {
  const t = title?.trim() ?? ''
  return t.length > 0 ? t : 'Untitled Prompt'
}
