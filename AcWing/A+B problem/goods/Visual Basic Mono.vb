Imports System

Module APlusB
    Sub Main()
        Dim ins As String() = Console.ReadLine().Split(New Char(){" "c})
        Console.WriteLine(Int(ins(0))+Int(ins(1)))
    End Sub
End Module
