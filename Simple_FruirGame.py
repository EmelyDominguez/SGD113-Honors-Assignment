namespace Simple_FruitStand
{
    class FruitStand
    {
        static void Main()
        {
            // Fruit stand menu
            Dictionary<string, double> menu = new Dictionary<string, double>
        {
            { "apple", 1.00 },
            { "banana", 0.50 },
            { "cherry", 0.25 },
            { "date", 0.75 },
            { "grape", 0.20 },
            { "kiwi", 1.50 },
            { "lemon", 0.30 },
            { "mango", 1.25 },
            { "orange", 0.80 },
            { "pear", 0.60 }
        };

            // Display the menu
            Console.WriteLine("Welcome to the Fruit Stand!");
            Console.WriteLine("Here is our menu:");
            foreach (var item in menu)
            {
                Console.WriteLine($"{item.Key}: ${item.Value:F2}");
            }

            // Initialize variables
            double totalCost = 0;
            string order = "";

            // While loop to take orders
            while (order.ToLower() != "done")
            {
                Console.Write("Enter the fruit you want to buy (or type 'done' to finish): ");
                order = Console.ReadLine().ToLower();
                if (menu.ContainsKey(order))
                {
                    Console.Write($"How many {order}s would you like? ");
                    int quantity = int.Parse(Console.ReadLine());
                    totalCost += menu[order] * quantity;
                    Console.WriteLine($"Added {quantity} {order}(s) to your order.");
                }
                else if (order != "done")
                {
                    Console.WriteLine("Sorry, we don't have that fruit.");
                }
            }

            // Display the total cost
            Console.WriteLine($"Your total cost is: ${totalCost:F2}");
            Console.WriteLine("Thank you for shopping with us!");
        }
    }
}
