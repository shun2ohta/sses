tell application "CotEditor"
    try
        set docName to name of front document
        display alert "ドキュメント名" message docName
    on error errMsg number errNum
        display alert "エラーが発生しました" message "エラー番号: " & errNum & " 内容: " & errMsg
    end try
end tell