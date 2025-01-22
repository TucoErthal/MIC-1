// if i <= n then x[i] := x[i] - y * 8

// if

    LODD i
    SUBD n
    JPOS else

// store original state

    LODD y
    PUSH

    LODD n
    PUSH

    LODD i
    PUSH

// calculate result

    // USANDO W provisoriamente
    // ac = y * 2
    LODL 2
    ADDL 2
    // ac *= 2
    PUSH
    ADDL 0
    // ac *= 2
    PUSH
    ADDL 0
    // W = y * 8
    INSP 2
    STOD W

    // USANDO Z provisoriamente!!!!!!!!!!!!
    //Z = x + i
    LODD x
    ADDD i
    STOD Z

    // USANDO SWAP, IMPOSSIVEL SEM!!!!!!!!!!!
    //n = sp original
    SWAP // ac = sp original, sp = x+i
    STOD n

    //i = m[x+i]
    LODL 0 // ac = m[x+i]
    SUBL W // ac = m[x+i] - y*8
    STOL 0 // m[x+i] = m[x+i] - y*8

    // undo swap
    LODD n //ac = sp
    SWAP // ac = m[x+i] - y*8, sp = sp

    // i = m[x+i] - y * 8
    LODD i
    SUBL 0
    STOD i
    INSP // y * 8 não vai ser usado novamente

    // m[x+i] = sp[0]
    LODD y
    SWAP // ac = sp, sp = y


    
    

// restore original state

else:
    //fim do programa    