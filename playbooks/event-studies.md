# Measure returns around an event

**Inputs.** An issuer event with an original publication timestamp, plus issuer and benchmark prices.

1. Convert the release time to the exchange timezone and assign the first tradable session. Handle after-close releases and holidays explicitly.
2. Freeze the expected-return baseline using earlier data. Measure realized and benchmark-relative returns on aligned windows.
3. Group repeated or overlapping events by issuer and flag confounding announcements, splits and trading halts.

**Acceptance check.** Move a synthetic release from before the close to after it. The eligible entry should move to the next tradable opportunity. Publish the event count alongside each estimate.

**Upstream resources.** [SEC EDGAR APIs (submissions, companyfacts, frames)](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) · [exchange_calendars](https://github.com/gerrymanoim/exchange_calendars) · [statsmodels](https://github.com/statsmodels/statsmodels)
