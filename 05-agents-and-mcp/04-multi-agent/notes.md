# Multi-agent patterns

## One-sentence truth

Two models is not automatically smarter. Multi-agent is useful when
roles or permissions are truly different, not when you want a vibe.

## Patterns that earn their keep

| Pattern | How | When |
|---|---|---|
| Supervisor | one model routes to specialists | different tools / prompts per role |
| Handoff | agent A finishes, B starts with a brief | pipeline stages |
| Critic | generator + independent checker | you can define "wrong" |
| Swarm | agents talk freely | rarely, and you will regret the logs |

## Costs

- n times the tokens
- failure modes become social ("they agreed on a wrong plan")
- debugging a conversation of six personas is miserable

## Course rule

One agent, well-tooled, beats three agents with opinions. We add a
second agent only when we can name the permission or eval it unlocks.
