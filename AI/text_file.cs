/// <summary>
/// Represents the entry point of the application and demonstrates usage of the <see cref="Text"/> class.
/// </summary>
public class Test
{
    /// <summary>
    /// The main entry point for the application.
    /// </summary>
    /// <param name="args">An array of command-line arguments.</param>
    public static void Main(string[] args)
    {
        // Create a new instance of the Text class
        Text text = new Text();

        // Add the first line of text
        text.AddText("Hello, world!");

        // Add the second line of text
        text.AddText("This is a test.");

        // Retrieve all concatenated text
        string allText = text.GetAllText();

        // Output the concatenated text to the console
        System.Console.WriteLine(allText);
    }
}

/// <summary>
/// Provides functionality to store and retrieve multiple lines of text.
/// </summary>
public class Text
{
    // Internal list to store lines of text
    private readonly System.Collections.Generic.List<string> lines = new System.Collections.Generic.List<string>();

    /// <summary>
    /// Adds a line of text to the collection.
    /// </summary>
    /// <param name="line">The line of text to add.</param>
    public void AddText(string line)
    {
        // Add the provided line to the list
        lines.Add(line);
    }

    /// <summary>
    /// Retrieves all lines of text concatenated with line breaks.
    /// </summary>
    /// <returns>A single string containing all lines separated by new lines.</returns>
    public string GetAllText()
    {
        // Join all lines with the system's newline separator
        return string.Join(System.Environment.NewLine, lines);
    }
}