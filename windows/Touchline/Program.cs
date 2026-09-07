namespace Touchline;
static class Program
{
    [STAThread]
    static void Main()
    {
        using var mutex = new Mutex(true, "Touchline.LiveScores.CurrentUser." + Environment.UserName, out bool first);
        if (!first) { MessageBox.Show("Touchline is already running. Open it from the system tray."); return; }
        ApplicationConfiguration.Initialize();
        Application.Run(new MainForm());
    }
}
