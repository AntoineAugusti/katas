calories =
  "data/01.txt"
  |> File.read!()
  |> String.split("\n")
  |> Enum.chunk_by(&(&1 == ""))
  |> Enum.reject(&(&1 == [""]))
  |> Enum.map(&Enum.reduce(&1, 0, fn v, acc -> acc + String.to_integer(v) end))

most = calories |> Enum.max()
top3 = calories |> Enum.sort(:desc) |> Enum.take(3) |> Enum.sum()

IO.puts(most)
IO.puts(top3)
