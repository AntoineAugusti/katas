input =
  "data/03.txt"
  |> File.read!()
  |> String.split("\n")
  |> Enum.reject(&(&1 == ""))

to_int = fn letter ->
  if String.upcase(letter) == letter do
    :binary.first(letter) - 38
  else
    :binary.first(letter) - 96
  end
end

input
|> Enum.map(&String.split_at(&1, round(String.length(&1) / 2)))
|> Enum.map(fn {a, b} ->
  MapSet.intersection(
    MapSet.new(a |> String.split("", trim: true)),
    MapSet.new(b |> String.split("", trim: true))
  )
end)
|> Enum.map(&(&1 |> MapSet.to_list() |> hd() |> to_int.()))
|> Enum.sum()
|> IO.inspect()
