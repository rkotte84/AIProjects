public class Test
{
    public static void Main(string[] args)
    {
        // Example usage of the Text class
        Text text = new Text();
        text.AddText("Hello, world!");
        text.AddText("This is a test.");
        
        string allText = text.GetAllText();
        System.Console.WriteLine(allText);
    }
}