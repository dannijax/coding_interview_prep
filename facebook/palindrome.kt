fun isPalindrome(str: String): Boolean {
    val start = 0
    val end = str.length -1
    var progress = false

    while(start <  end){
        progress = str.get(start) == str.get(end)

    }

    return progress

}