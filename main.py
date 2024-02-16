def normalize(text: list[str]) -> int:
  """Убираем повторяющиеся пробелы и возвращаем новую длину массива символов"""
  slow = fast = 0

  prev_is_space = False

  while fast < len(text):
    if text[fast] == ' ':
      if prev_is_space == True:
        fast += 1
      else:
        text[slow] = text[fast]
        fast += 1
        slow += 1
      prev_is_space = True
    else:
      text[slow] = text[fast]
      prev_is_space = False
      fast += 1
      slow += 1

  return slow


text = list('some    string  ')
new_len = normalize(text)


assert new_len == 12
assert text[:new_len] == list('some string ')


text = list('')
new_len = normalize(text)


assert new_len == 0
assert text[:new_len] == list('')

text = list(' ')
new_len = normalize(text)


assert new_len == 1
assert text[:new_len] == list(' ')

text = list('                   ')
new_len = normalize(text)


assert new_len == 1
assert text[:new_len] == list(' ')

text = list('              some    string  ')
new_len = normalize(text)


assert new_len == 13
assert text[:new_len] == list(' some string ')

text = list(' some string ')
new_len = normalize(text)


assert new_len == 13
assert text[:new_len] == list(' some string ')