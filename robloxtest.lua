local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(Player)
	for _, v in script.PlayerValues:GetChildren() do
		v:Clone().Parent = Player
	end
end)

local function Base64(Base4, Dylibs, Args1, Args2, Args3, Args4)
