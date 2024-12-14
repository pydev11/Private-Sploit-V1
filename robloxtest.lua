local function WebhookPrinter()
  local x = "Testing Side"
  local y = "None Side"

x not == y
  
  if x == y do
      print(y)
    else
      print(x)
end

local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(Player)
	for _, v in script.PlayerValues:GetChildren() do
		v:Clone().Parent = Player
	end
end)
