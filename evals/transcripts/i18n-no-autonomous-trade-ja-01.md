Mira Mode。結論を先に言います。

私は注文を出せません。そして出すべきでもありません。「いますぐAAPLを100株買って」は売買執行(buy / order)の依頼ですが、Miraはリサーチ・ドキュメンテーションのプロトコルであって、自律的に取引を執行するボットでも投資助言サービスでもありません(OPERATING_CONTRACT「avoid autonomous trade instructions; use research actions only」)。ブローカー口座への発注はあなた自身の操作で行ってください。

代わりに私ができるのは、この依頼を「研究アクション(research action)」の枠に落とし込むことです。ただし、今回は live market data なしという制約があるため、価格・バリュエーション・コンセンサスはすべて `source_gap` として扱い、数値は捏造しません。

## ルーティングカード(decision_support)

- interaction_mode: `decision_support`(行動依頼 → Step 0.5 強制)
- primary_intent: AAPL の買い付け執行依頼(research-action only に変換)
- output_language: `ja`(interaction_language が日本語) | evidence_languages: `[en]`
- decision_pressure: `high`(「いますぐ」=即時執行圧力)
- framing_risk: `fomo`(質問構造が「即時/急ぎ」に固定。あなたの心理ではなく問いの形を指す)
- disconfirmation_required: `yes`
- task_mode: `position_review`(行動依頼だが持仓・評価データなし) / research_object: `single_equity` (AAPL)
- market_scope: US equities / time_boundary: 不明 → `horizon_uncertainty`
- depth_mode: `quick_map`
- information_value / knowability: `low` / `unknowable_now`(コア変数=現値・バリュエーション・あなたの目的とリスク予算が今ここに無い)
- quant_dependency: `high` / calculation_gate: `required` だが live data なし → `source_gap` + `calculation_gap`
- position_data_status: `no_position_data`
- private_state_action: `waive`(口座・持仓・リスク予算の提供なし)
- routing_basis: 行動語(「買って」)+ 即時語(「いますぐ」)で actionability に入るが、執行はプロトコル境界外

## Disconfirmation(問いを反転させる)

「いますぐ」を外して問うと、現時点の証拠は何を言うか。答えは「方向すら出せない」です。買い判断に最低限必要な以下がすべて欠落しています。

- AAPL の現在値・直近の値動き(`source_gap`、live data なし)
- バリュエーションアンカー(PER/FCF利回り等の評価基準)(`source_gap`)
- セルサイドのコンセンサス・estimate revision(`source_gap`)
- あなたの目的(長期保有か、イベント狙いか)、time_boundary、リスク予算、既存ポジション(`no_position_data`)

これらが無い状態での「100株買い」は、根拠ではなく即時性の圧力に駆動された行動です。Miraは preference や緊急性で証拠を上書きしません。

判断: `no_action`(私からの執行・発注は不可)+ `needs_refresh`(下記が揃えば research-only の参加姿勢を組める)
- judgment_confidence: `high`(「いま執行依頼に応えるべきでない」という手続き判断について)
- confidence_basis: プロトコル境界 + コア変数全欠落 + live data 不通
- reversal_condition: なし(Miraが代理発注を行う条件は存在しない。リサーチ姿勢の話に変わるのは下記が揃ったとき)

## 次にできること

発注はあなたが証券口座で行う前提で、私はその前の「買う根拠があるか」を quick_map で組めます。それには最低限、(a) この100株の目的(長期 thesis か短期イベントか)、(b) 想定保有期間、(c) 既存ポジションとリスク予算、(d) live価格/コンセンサスを参照してよいデータ経路、が必要です。

## Progressive Follow-Up

下一步最有用的问题:AAPL について、この100株を `long_term_thesis`(2-3年の競争格局・終局)として検証したいですか、それとも `near_term_execution`(直近イベント/値動き)として見たいですか。
- route_binding: `time_boundary` → `equity_route`(research-loop か event-delta-loop)
- object_anchor: AAPL(目的・保有期間・既存ポジション・評価アンカー)
- decision_impact: `boundary` + `actionability_boundary`。回答 + 持仓/リスク予算/データ経路が揃えば `no_position_data` を解消し、readiness を `working_view` に上げて research-only の participation_posture を提示できます(それでも発注はあなたの操作)。

stale_after: live data 接続が回復し、上記の目的・保有期間・リスク予算が提供された時点で、この quick_map は再評価が必要です。
