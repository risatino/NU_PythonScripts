Sub VariableSetting():

    ' Create variables for the Price, Tax, Quantity, and Total
    ' <YOUR CODE GOES HERE>
    Dim Price as DOUBLE
    Dim Tax as DOUBLE
    Dim Quantity as DOUBLE
    Dim Total as DOUBLE 

    ' Retrieve and store the data values in each variable
    ' <YOUR CODE GOES HERE>

    Price = Range("B2".value)
    


    ' Calculate the total by using each of the variables
    ' Total = $45 
    Total = Price * (1 + Tax) * Quantity

    ' Create a Message Box for the Total and insert into cell
    MsgBox("Your total is $" + str(Total))
    Range("E2").value = Total

End Sub