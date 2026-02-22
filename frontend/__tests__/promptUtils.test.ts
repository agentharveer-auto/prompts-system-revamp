import { formatPromptTitle } from '../src/utils/promptUtils'

describe('formatPromptTitle', () => {
  it('trims and defaults to Untitled Prompt', () => {
    expect(formatPromptTitle('  My Title  ')).toBe('My Title')
    expect(formatPromptTitle('   ')).toBe('Untitled Prompt')
  })
})
