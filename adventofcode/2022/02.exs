input =
  "data/02.txt"
  |> File.read!()
  |> String.split("\n")
  |> Enum.reject(&(&1 == ""))

possibilities = for x <- ~w(A B C), y <- ~w(X Y Z), do: "#{x} #{y}"

unless MapSet.equal?(MapSet.new(possibilities), MapSet.new(input)) do
  raise "unexpected input"
end

# Part 1
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
input
|> Enum.map(
  &Map.fetch!(
    %{
      "A X" => 1 + 3,
      "A Y" => 2 + 6,
      "A Z" => 3 + 0,
      "B X" => 1 + 0,
      "B Y" => 2 + 3,
      "B Z" => 3 + 6,
      "C X" => 1 + 6,
      "C Y" => 2 + 0,
      "C Z" => 3 + 3
    },
    &1
  )
)
|> Enum.sum()
|> IO.inspect()

# Part 2
input
|> Enum.map(
  &Map.fetch!(
    %{
      "A X" => 0 + 3,
      "A Y" => 3 + 1,
      "A Z" => 6 + 2,
      "B X" => 0 + 1,
      "B Y" => 3 + 2,
      "B Z" => 6 + 3,
      "C X" => 0 + 2,
      "C Y" => 3 + 3,
      "C Z" => 6 + 1
    },
    &1
  )
)
|> Enum.sum()
|> IO.inspect()
