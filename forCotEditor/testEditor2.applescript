tell application "CotEditor"
    try
        -- 現在の日時を取得（文字列として）
        set currentDate to do shell script "date '+最終更新日時: %Y-%m-%d %H:%M:%S'"
        
        -- アクティブなドキュメントを取得
        set currentDoc to front document
        
        -- 選択範囲の有無を確認
        if length of (selected range of currentDoc) > 0 then
            -- 選択範囲がある場合は置き換え
            set selection of currentDoc to currentDate
        else
            -- 挿入ポイントに日時を挿入
            tell currentDoc
                insert currentDate at after insertion point
            end tell
        end if
    on error errMsg number errNum
        -- エラーが発生した場合は詳細を表示
        display alert "エラーが発生しました" message "エラー番号: " & errNum & " 内容: " & errMsg
    end try
end tell