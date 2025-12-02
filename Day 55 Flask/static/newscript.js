let customPrompt;

function myFunction(buttonId) {
    // Text Options
    if (buttonId == "streamable") {
        var copyandpaste =
`Test
String
Multiline`;
    } else if (buttonId == "2") {
        var copyandpaste = "> **Denied. Unusable Evidence Format / Invalid or no Video / Broken Link** \n" +
        "> \n" +
        "> Section A-II. \n" +
        "> Evidence **must be included** in the ticket, and the evidence shall be in **video** format via the following: \n" +
        "> > Medal.tv, \n" +
        "> > Youtube.com \n" +
        "> **Streamable is not supported as a format** \n" +
        "> Video must show fullscreen (UIs, Leaderboard and Etc.) \n" +
        "> \n" +
        "> (**Discord attachment is not allowed**) ( **We need to archive and record the video link**) \n" +
        "> \n" +
        "> Screenshots cannot be used as proof unless it serves as supplementary evidence to provide context to an associated video. \n" +
        "> \n" +
        "> Clip must show full screen and all text must be eligible on the UI \n" +
        "> \n" +
        "> **Please remake the ticket once evidence is in correct format**, Do **NOT** use streamable.com as the video expires itself and log archives is required. \n" +
        "> \n" +
        ">  https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub";
    } else if (buttonId == "allies") {
        console.log("Allies")
        let customPrompt = prompt("Enter message you want player to say:");
        var copyandpaste = 
`> Hello!
> Please go ingame and say \`${customPrompt}\`
> Then I can restore you`;
    } else if (buttonId == "4") {
        var copyandpaste = "> **Denied. No Death screen / Death splash ID** \n" +
        "> \n" +
        "> A-IV. Death Splash User Interface (UI) \n" +
        "> The video evidence shall include the death splash UI for it to be a valid restore.\n" +
        "> \n" +
        "> The following evidence is not sufficient for leniency as major proofs are required for it to be valid. With leniency clause attributed to non-NPC deaths \n"+
        "> \n" +
        "> **Please remake the ticket if you have video proof or screen to accompany the rest of the video** \n" +
        "> \n" +
        "> https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub \n";
    } else if (buttonId == "5") {
        var copyandpaste = "> **Denied. Need your own POV** \n" +
        "> \n" +
        "> A-III. Point of View (POV) \n" +
        "> Players are required to use their own POV clips for restores. \n" +
        "> \n " +
        "> https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub";
    } else if (buttonId == "6") {
        var copyandpaste = "> **Denied. Does not show how you got stuck/flung** \n" +
        "> \n" +
        "> H-I. General \n" +
        "> Any instance where a player is stuck in the floor, wall, or blocks is restorable. The player must however show **how they got stuck** with video evidence. \n" +
        "> \n" +
        "> If a player shows evidence of them being stuck, but they do not show how they > got stuck, they may not be restored. \n" +
        "> \n" +
        "> **If you have evidence showing how you got stuck, make a new ticket** \n" +
        "> \n" +
        " > https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub";
    } else if (buttonId == "7") {
        var copyandpaste = "> **Denied. ineligible UI/Text** \n" + 
        ">  A-II. Video Evidence \n" +
        "> .... The video evidence shall not be cropped in any way; AND all UI/text on screen must be legible, otherwise the restore can be denied.\n" +
        "> \n" +
        "> https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub";
    } else if (buttonId == "8") {
        var copyandpaste = "> **Denied. Player needs their own ticket** \n" +
        "> \n" +
        "> If a player makes a ticket for a restorable death, they must be making it for an account/slot that they own. ***Players cannot make tickets for their friends or other people***. If a player is making a ticket for an account they are not Discord-verified to (verification issue, alternate account, etc.), they should prove that the account is theirs. \n" +
        "> \n" +
        "> https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub"
    } else if (buttonId == "9") {
        var copyandpaste = "> ** Section A-IX; Second clause in effect** \n"
        "> \n"
        "> A-IX. Second Opinions \n"
        "> The player may create a second ticket only once if they believe their situation is > restorable. The player must request a different moderator to look into their evidence. \n"
        "> \n"
        "> Players shall not abuse the ticket system. If a player makes more than two tickets regarding the same evidence, moderators may warn and ban them according to Rule 1.9 in the ban rulebook. \n"
        "> \n"
        "> https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub \n";
    } else if (buttonId == "10") {
        var copyandpaste = "> **Denied. Death imminent** \n" +
        "> \n" +
        "> **A-XI. Marked for Death** \n" +
        "> In a scenario where death is imminent for a player and a bug (or otherwise restorable instance) occurs, the player may not be eligible for a restore if the bug/ping lag had little impact on the outcome. AND/OR player was already Low HP / Very unlikely to survive the death nevertheless \n" +
        "> \n" +
        "> https://docs.google.com/document/d/e/2PACX-1vQUwjgPHEqZ_Ok8N9x_cYv9jm27Ln2pcPepOPtuFFXk8rbkuShDlVADoTw_hIjwlNA0itXTa5-6R7Q6/pub";
    }

    navigator.clipboard.writeText(copyandpaste);

    var copybutton = document.getElementById(buttonId);
    // Alert the copied text
    // alert("Copied the text: " + copybutton.value);
  }