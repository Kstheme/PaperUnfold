# Progress format example

`progress-format-example.json` is a **hand-authored format example**, with fictional
researcher answers. It is not an executed teaching transcript or learning result.
Its source points to the repository's readable excerpt fixture.

Read it together with its source, without creating or updating a progress file:

```text
python skills/paper-tutor/scripts/progress.py resume examples/paper-tutor/progress-format-example.json
```

An actual resume invocation can supply the record and readable excerpt to
`paper-tutor`, then ask it to continue from the weights-versus-output gap. The
calculation evidence supports only that toy calculation. The gap survives pause,
end, and a change of conversation. File structure validation cannot establish
the accuracy of the teacher's assessment; compare it with the actual answers.
